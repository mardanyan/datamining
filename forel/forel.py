
import random

class FOREL:

    def dist2(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return dx * dx + dy * dy

    def recluster(self, points, radius):
        result = []
        random.random()
        r2 = radius * radius;
        unclustered = points

        while len(unclustered) > 0:
            newCenter = unclustered[random.randint(0, len(unclustered) - 1)]

            while True:
                center = newCenter
                x, y = 0.0, 0.0
                cnt = 0
                for p in unclustered:
                    if self.dist2(center, p) < r2:
                        x += p[0]
                        y += p[1]
                        cnt += 1
                newCenter = (x/cnt, y / cnt)
                if center == newCenter:
                    break

            cluster = []
            # print("unclus: " + str(len(unclustered)))
            # print(unclustered)
            i = 0
            while i < len(unclustered):
                print(i)
                print(unclustered[i])
                if self.dist2(center, unclustered[i]) < r2:
                    cluster.append(unclustered[i]);
                    del unclustered[i]
                else:
                    i += 1

            print(center)
            result.append([center[0], center[1], radius])
        return result


