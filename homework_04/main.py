"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from models import engine, User, Post, Session
import models
import sys
from jsonplaceholder_requests import get_json_data, log


async def create_tables():
    """
    If we aren't using alembic
    """
    try:
        async with engine.begin() as conn:
            await conn.run_sync(models.Base.metadata.drop_all)
            await conn.run_sync(models.Base.metadata.create_all)
        return True
    except Exception as e:
        log.error(e)
        return False


async def write_users_to_db(users_data) -> models.User:
    """
    :param users_data:
    """
    log.info("write users to db")
    async with Session() as session:
        async with session.begin():
            users: list[User] = []
            for user_data in users_data:
                user = User(
                    id=int(user_data['id']),
                    email=user_data['email'],
                    name=user_data['name'],
                    username=user_data['username'],
                    phone=user_data['phone'],
                    website=user_data['website'],
                )
                users.append(user)
            session.add_all(users)


async def write_posts_to_db(posts_data) -> models.Post:
    """
    :param posts_data:
    """
    # user = models.User(user_data=user_data)
    log.info("write users to db")
    async with Session() as session:
        async with session.begin():
            posts: list[Post] = []
            for post_data in posts_data:
                post = Post()
                post.id = int(post_data['id'])
                post.user_id = int(post_data['userId'])
                post.body = post_data['body']
                post.title = post_data['title']
                posts.append(post)
            session.add_all(posts)


async def async_main():
    # Get users and from https://jsonplaceholder.typicode.com
    users_data, posts_data = await get_json_data()
    if users_data is None or posts_data is None:
        log.error('Can not receive users or posts data.')
        sys.exit(1)
    # Create tables in DB
    result_create_tables = await create_tables()
    if not result_create_tables:
        log.error('Can not create tables in DB.')
        sys.exit(1)

    await write_users_to_db(users_data)
    await write_posts_to_db(posts_data)


def main():
    asyncio.get_event_loop(). \
        run_until_complete(async_main())


if __name__ == "__main__":
    main()
