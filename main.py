from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


OPENWEATHER_KEY = "afec6a554ab5fc9f18e84596dcb898b9"

@app.get("/clima/{consulta}")
async def clima(consulta: str):
    try:
        async with httpx.AsyncClient() as client:
            if consulta.isdigit():
                response_cep = await client.get(f"https://viacep.com.br/ws/{consulta}/json/")
                response_cep.raise_for_status()
                dados_cep = response_cep.json()
                cidade = dados_cep["localidade"]
                uf = dados_cep["uf"]
            else:
                cidade = consulta
                uf = ""

            response_geo = await client.get(
                "http://api.openweathermap.org/geo/1.0/direct",
                params={
                    "q": f"{cidade},{uf},BR" if uf else f"{cidade},BR",
                    "limit": 1,
                    "appid": OPENWEATHER_KEY
                }
            )
            response_geo.raise_for_status()
            geo = response_geo.json()

            if not geo:
                return {"erro": "Localização não encontrada"}

            lat, lon = geo[0]["lat"], geo[0]["lon"]
            cidade_nome = geo[0]["name"]
            uf_final = geo[0].get("state", "Desconhecido")

            response_weather = await client.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "lat": lat,
                    "lon": lon,
                    "appid": OPENWEATHER_KEY,
                    "units": "metric",
                    "lang": "pt_br"
                }
            )
            response_weather.raise_for_status()
            clima = response_weather.json()

            return {
                "cidade": cidade_nome,
                "uf": uf_final,
                "temperatura": f"{clima['main']['temp']}°C",
                "clima": clima['weather'][0]['description'],
                "umidade": f"{clima['main']['humidity']}%",
                "vento": f"{clima['wind']['speed']} m/s"
            }

    except Exception as e:
        return {"erro": str(e)}