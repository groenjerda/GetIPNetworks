from sqlalchemy.ext.asyncio import AsyncSession

from .models import AsInfo


class CRUDASInfo:
    async def write(
        self, as_info: AsInfo, async_session: AsyncSession
    ) -> None:
        async with async_session() as session:
            await session.add(as_info)
            await session.commit()


asinfo_crud = CRUDASInfo()
