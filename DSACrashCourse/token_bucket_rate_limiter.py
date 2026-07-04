# Do NOT implement
from time import time


class HttpServer:
    def __init__(self):
        self._limiter = RateLimiter(max_tokens=1000, refresh_rate=10)

    def POST(self, request):
        if self._limiter.can_serve_request(request.num_tokens_required, request.timeout):
            # do stuff
            return 200  # HTTP Status Code OK
        else:
            return 429  # HTTP Status Code for rate limiting


# TODO: Implement
class RateLimiter:
    """
    - You start with 1000 tokens.
    - You can only hold max 1000 tokens.
    - Each request consumes tokens.
    - New tokens are generated continuously, at a rate of 10 new tokens per second.
    - If there are not enough tokens available, sleep until enough tokens become available, or the timeout is reached.
    """
    def __init__(self, max_tokens=1000, refresh_rate=10):
        self.total_tokens_in_bucket = max_tokens
        self.max_tokens = max_tokens
        self.refresh_rate = refresh_rate
        self.last_refill = time.time()

    def can_serve_request(self, num_tokens_required: int, timeout_sec: float) -> bool:
        self._refill_tokens()
        if num_tokens_required > self.max_tokens:
            return False
        if num_tokens_required <= self.total_tokens_in_bucket:
            self.total_tokens_in_bucket -= num_tokens_required
            return True
        if num_tokens_required > self.total_tokens_in_bucket:
            shortage_tokens = num_tokens_required - self.total_tokens_in_bucket
            generate_token_during_sleep = self.refresh_rate * timeout_sec
            if shortage_tokens > generate_token_during_sleep:
                return False
            min_sleep_needed = shortage_tokens / self.refresh_rate
            time.sleep(min_sleep_needed)
            self._refill_tokens()
            self.total_tokens_in_bucket -= num_tokens_required
            return True
        
    def _refill_tokens(self):
        elapsed_time = time.time() - self.last_refill
        tokens_to_add = elapsed_time * self.refresh_rate
        self.total_tokens_in_bucket = min (self.max_tokens, self.total_tokens_in_bucket + tokens_to_add)
        self.last_refill = time.time()