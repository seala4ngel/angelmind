from concurrent.futures import ThreadPoolExecutor, as_completed

class Threader:
    def __init__(self, max_workers=50):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def run(self, func, items):
        futures = {self.executor.submit(func, item): item for item in items}
        results = []
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                results.append({"error": str(e)})
        return results
