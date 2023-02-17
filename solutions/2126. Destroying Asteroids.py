class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for am in sorted(asteroids):
            if mass>=am:
                mass+=am
            else:
                return False
        return True
