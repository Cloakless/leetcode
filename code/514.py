class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R = len(ring)
        K = len(key)

        min_dists = {}
        search_results = {}

        # Cost of finishing given we are at r on the ring and need 
        # to spell out the answer from the kth character
        def search(r, k):
            if (r, k) in search_results:
                return search_results[(r, k)]
            if k == K:
                # already finished
                search_results[(r, k)] = 0
                return 0

            elif ring[r] == key[k]:
                search_results[(r, k)] = search(r, k+1) + 1
                return search_results[(r, k)]
            else:
                # Minimum path is of same length as one which includes nearest one
                # on one side or another
                target = key[k]
                if (r, target) in min_dists:
                    (rc, ra, dist_clockwise, dist_alockwise) = min_dists[(r, target)]
                else: 
                    dist_clockwise = 0
                    dist_alockwise = 0
                    rc = r
                    ra = r
                    found_cw = False
                    found_aw = False
                    while not found_cw:
                        rc += 1
                        dist_clockwise += 1
                        if rc == R:
                            rc = 0
                        if ring[rc] == target:
                            found_cw = True
                    while not found_aw:
                        ra -= 1
                        dist_alockwise += 1
                        if ra == -1 :
                            ra = R-1
                        if ring[ra] == target:
                            found_aw = True
                    min_dists[(r, target)] = (rc, ra, dist_clockwise, dist_alockwise)
                if rc == ra:
                    dist = min(dist_clockwise, dist_alockwise)
                    search_results[(r, k)] =  search(rc, k+1) + dist + 1
                    return search_results[(r, k)]
                else:
                    search_results[(r, k)] =  min(search(rc, k+1) + dist_clockwise + 1, search(ra, k+1) + dist_alockwise + 1)
                    return search_results[(r, k)]
        return search(0,0)
