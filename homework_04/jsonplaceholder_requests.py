import asyncio
import logging
from dataclasses import dataclass
from typing import Optional, List
from aiohttp import ClientSession, ClientTimeout

DEFAULT_FORMAT = "%(asctime)s %(levelname)-8s [%(name)-8s] (%(filename)s:%(funcName)s:%(lineno)d) %(message)s"

logging.basicConfig(format=DEFAULT_FORMAT, level=logging.DEBUG)

log = logging.getLogger(__name__)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class Service:
    name: str
    url: str


SERVICES = [
    Service("users", USERS_DATA_URL),
    Service("posts", POSTS_DATA_URL),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    try:
        async with session.get(url) as response:
            result = await response.json()
    except Exception as e:
        log.error(e)
        return None
    return result


async def fetch_users_data(service: Service) -> Optional[str]:
    log.info("Fetch json data from service %r", 'users')
    session_timeout = ClientTimeout(total=500, sock_connect=10, sock_read=10)
    async with ClientSession(timeout=session_timeout) as session:
        json_data = await fetch_json(session, service.url)
    log.info("Fetched json data from service %r: %s", service.name, json_data)

    return json_data


async def fetch_posts_data(service: Service) -> Optional[str]:
    log.info("Fetch json data from service %r", 'posts')
    session_timeout = ClientTimeout(total=500, sock_connect=10, sock_read=10)
    async with ClientSession(timeout=session_timeout) as session:
        json_data = await fetch_json(session, service.url)
    log.info("Fetched json data from service %r: %s", service.name, json_data)

    return json_data


async def get_json_data():
    tasks = [
        fetch_users_data(SERVICES[0]),
        fetch_posts_data(SERVICES[1])
    ]

    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(*tasks)
    if users_data is not None and posts_data is not None:
        return users_data, posts_data
    else:
        return None


def main():
    users_data, posts_data = asyncio.get_event_loop().run_until_complete(get_json_data())
    log.info("finished main")


if __name__ == '__main__':
    main()
