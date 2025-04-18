from rapidfuzz import process

ListeRareté = [
    'Tout', 'Common', 'Rare', 'Parallel Rare', 'Starfoil Rare', 'Mosaic Rare', 'Shatterfoil',
    'Super Rare', 'Super Parallel Rare', 'Ultra Rare', 'Ultra Parallel Rare', 'Gold Rare',
    'Premium Gold Rare', 'Gold Secret Rare', 'Secret Rare', 'Secret Parallel Rare',
    'Extra Secret Rare', 'Platinum Rare', 'Platinum Secret Rare', 'Collectors Rare',
    'Quarter Century Secret Rare', 'Ultimate Rare', 'Ghost Rare', 'Starlight Rare',
    'Holographic Rare', 'Special', 'Token', 'Oversized', 'Unknown'
]
print(process.extractOne("gold rare",ListeRareté))
# Retourne par ex : ('Ultimate Rare', 96.0, 1)
