import socket
import redis.asyncio as aioredis
from datetime import datetime

redis_client = aioredis.Redis(
    host="127.0.0.1",
    port=6379,
    decode_responses=True,
    protocol=2,
    socket_timeout=3.0
)

def getLocalIP():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sc:
            return  sc.getsockname()[0]
        
    except Exception as e:    
        return "127.0.0.1" # 실패 시 루프백 반환
    
    finally:
        sc.close()

def isNullOrWhiteSpace(s : str) -> bool:
    return not s or not s.strip()

async def GenerateChartNo() -> str:
    """
        현재날짜(8자리) + 순번(4자리) 조합의 차트번호 생성
        :return: 생성된 차트번호 (총 12자리)
    """

    # 현재 날짜 구하기
    nowDT = datetime.now()
    strDT = nowDT.strftime("%Y%m%d")

    # Redis 를 이용한 다잉ㄹ 기준 시퀀스 발급
    redis_key = f"chart_seq:{strDT}"

    # incr 명령어로 값을 1씩 증가시킴
    seqNo = await redis_client.incr(redis_key)

    # 처음 생성된 키라면 다음날 데이터 정리를 위해 24시간 뒤에 만료되도록 설정
    if seqNo == 1:
        redis_client.expire(redis_key, 86400)

    # 순번을 4자리 문자열로 패딩
    strSeq = f"{seqNo:04d}"

    # 최종 차트번호 셍상
    chartNo = f"{strDT}{strSeq}"

    return chartNo