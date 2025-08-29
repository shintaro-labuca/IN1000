#a)
print("Hva er favorittfargen din?")
favorittfarge = input("Skriv her: ").lower()
frukter = {
    "gul": "banan",
    "oransje": "appelsin",
    "gronn": "guava"
}


#b)

if favorittfarge in frukter:
    print(f"Her er en frukt basert på din favorittfarge: {frukter[favorittfarge]}")
else:
    print("idk")


'''
funnet = False

for farge, frukt in frukter.items():
    if farge == favorittfarge:
        print(f"Her en en frukt basert på din favorittfarge: {frukt}")
        funnet = True
        break
if not funnet:
       print("idk")
'''
    
    

