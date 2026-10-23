"""Deterministic, explainable outfit combinations from local inventory."""
from itertools import product

COMPLEMENTARY = {
 'black': {'white','grey','gray','beige','red','blue'},
 'white': {'black','navy','blue','brown','green'},
 'navy': {'white','beige','grey','gray','brown'},
 'blue': {'white','black','beige','brown'},
 'beige': {'navy','black','white','brown'},
}

def suggest_outfits(garments: list[dict], occasion='casual', season='all', limit=10) -> list[dict]:
    """Rank top/bottom/shoes sets without external models or network requests."""
    if not 1 <= limit <= 100: raise ValueError('limit must be between 1 and 100')
    compatible=[g for g in garments if g.get('season','all') in ('all',season) and g.get('occasion','casual') in (occasion,'all','casual')]
    groups=[]
    for cats in ({'top','shirt','tshirt','blouse'},{'bottom','pants','trousers','skirt','jeans'},{'shoes','footwear','sneakers','boots'}):
        groups.append([g for g in compatible if g['category'] in cats])
    scored=[]
    for trio in product(*groups):
        colors=[g['color'].lower() for g in trio]
        score=50 + sum(8 for g in trio if g.get('favorite'))
        score+=sum(10 for a,b in ((0,1),(0,2),(1,2)) if colors[b] in COMPLEMENTARY.get(colors[a],set()) or colors[a] in COMPLEMENTARY.get(colors[b],set()))
        score-=sum(min(int(g.get('wears',0)),20) for g in trio)//3
        scored.append({'garment_ids':[g['id'] for g in trio], 'garments':list(trio),'score':min(100,score), 'reason':'Color coordination, favorites and wear rotation'})
    return sorted(scored,key=lambda s:(-s['score'],s['garment_ids']))[:limit]
