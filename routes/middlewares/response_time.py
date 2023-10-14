import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response


def time_diff_to_human_readable_format(start_time: time, end_time: time) -> str:
    """
    returns end_time - start_time in ms, ns and such and never return more than two decimals
    """
    t = end_time - start_time
    if t < 0.001:
        return f"{t * 1000 * 1000:.2f} ns"
    elif t < 1:
        return f"{t * 1000:.2f} ms"
    else:
        return f"{t:.2f} s"


class ResponseTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()
        response = await call_next(request)
        end_time = time.time()
        response.headers["X-HTTP-Response-Time"] = time_diff_to_human_readable_format(
            start_time, end_time
        )
        return response


