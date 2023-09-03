from collections import Counter

n = int(input())
colors = list(map(int, input().split()))

color_counts = Counter(colors)
min_color_count = min(color_counts.values())
min_colors = [color for color, count in color_counts.items() if count == min_color_count]

min_color = min(min_colors)

print(min_color)
