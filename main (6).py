[9/23, 3:14 PM] Santhosh Frd: l1=['shoes','cars','laptop']

for i,j in enumerate(l1):
  print(i,j)
[9/23, 3:14 PM] Santhosh Frd: def LinearSearchProduct(productList, targetProduct):
    indices = []

    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)

    return indices

# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = LinearSearchProduct(products, target)
print(result)