from contextlib import asynccontextmanager
from typing import Any, Dict, Optional

import aiohttp

from core.config import settings

@asynccontextmanager
async def do_request(
    url: str,
    json: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, Any]] = None,
    method: str = 'POST'
) -> Any:
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    final_exc = None
    async with aiohttp.ClientSession(
        connector=connector,
        timeout=timeout
    ) as session:
        for _ in range(settings.RETRY_COUNT):
            try:
                print(f"Making request to {url} with method {method}")
                print(f"Headers: {headers}")
                print(f"Payload: {json}")
                async with session.request(
                    method,
                    url,
                    json=json,
                    headers=headers,
                ) as response:
                    print(f"Response status: {response.status}")
                    yield response
                    return
            except aiohttp.ClientResponseError as exc:
                print(f"Request failed: {exc}")
                final_exc = exc

    await session.close()
    if final_exc is not None:
        raise final_exc
    raise RuntimeError('Unsupported')


@asynccontextmanager
async def do_request_get(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, Any]] = None,
    method: str = 'POST'
) -> Any:
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    final_exc = None
    async with aiohttp.ClientSession(
        connector=connector,
        timeout=timeout
    ) as session:
        for _ in range(settings.RETRY_COUNT):
            try:
                print(f"Making request to {url} with method {method}")
                print(f"Headers: {headers}")
                print(f"Params: {params}")
                async with session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                ) as response:
                    print(f"Response status: {response.status}")
                    yield response
                    return
            except aiohttp.ClientResponseError as exc:
                print(f"Request failed: {exc}")
                final_exc = exc

    await session.close()
    if final_exc is not None:
        raise final_exc
    raise RuntimeError('Unsupported')