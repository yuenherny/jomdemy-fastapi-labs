import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        token = "xxxxxxx"
        response = await client.get(f"http://localhost:8000/event/all/{token}")
        print("status code", response.status_code)
        print("response body", response.text)


asyncio.run(main())