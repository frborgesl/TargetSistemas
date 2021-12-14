sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
outros = 19.84953
total = sp + rj + mg + es + outros
print(f"O valor total mensal foi R${total}")

conta_sp = ((sp/total)*100)
conta_rj = ((rj/total)*100)
conta_mg = ((mg/total)*100)
conta_es = ((es/total)*100)
conta_outros = ((outros/total)*100)

print(f'Porcentagem de SP {conta_sp:.2f}%')
print(f'Porcentagem de RJ {conta_rj:.2f}%')
print(f'Porcentagem de MG {conta_mg:.2f}%')
print(f'Porcentagem de ES {conta_es:.2f}%')
print(f'Porcentagem de OUT {conta_outros:.2f}%')