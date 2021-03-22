koz_count = int(input())
eggs_count = int(input())
kurab_kg = int(input())
kozunak = koz_count * 3.20
eggs_12 = eggs_count * 4.35
kurabii = kurab_kg * 5.40
paint_for_egg = 0.15
total_paint = eggs_count * 12 * paint_for_egg
total = kozunak + eggs_12 + kurabii + total_paint
print(f"{total:.2f}")
