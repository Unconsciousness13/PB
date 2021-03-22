caterpillar_groups_count = int(input())
musala = 0
montblank = 0
kilimanjaro = 0
k2 = 0
everest = 0
caterpillars_sum = 0
for number in range(caterpillar_groups_count):
    caterpillars = int(input())
    caterpillars_sum += caterpillars
    if caterpillars <= 5:
        musala += caterpillars
    if 6 <= caterpillars <= 12:
        montblank += caterpillars
    if 13 <= caterpillars <= 25:
        kilimanjaro += caterpillars
    if 26 <= caterpillars <= 40:
        k2 += caterpillars
    if caterpillars > 40:
        everest += caterpillars
print(f"{(musala / caterpillars_sum) * 100:.2f}%")
print(f"{(montblank / caterpillars_sum) * 100:.2f}%")
print(f"{(kilimanjaro / caterpillars_sum) * 100:.2f}%")
print(f"{(k2 / caterpillars_sum) * 100:.2f}%")
print(f"{(everest / caterpillars_sum) * 100:.2f}%")
