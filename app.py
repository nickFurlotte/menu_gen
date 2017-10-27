
import os

from flask import Flask, render_template, Markup
import numpy as np
import pandas as pd

app = Flask(__name__)

foods = pd.read_csv('foods_filter_names.csv')
flavors = pd.read_csv('flavors.csv')

flavor_names = flavors.name.values.flatten()
food_names = foods.name.values.flatten()
cooking_styles = [

    'grilled','fried','deep fried', 'braised','skillet fried','pan fried','boiled','steamed','sous vide','flambee','fast fry','foamed','deconstructed','scraped','quickened',
    'blistered','lifted','locally sourced','beer braised','assorted','tossed','sprouted',
    'rubbed'

]

cooking_styles2 = [
    'British','American','Thai','Chinese','Southern','Mid-Western','Indian', "Creole",'Greek','Middle Eastern', 'gluten free','Mexican','TexMex','French',
    'Southern Trailer Park','Late Summer','rustic','homespun','market','virgin',
    'farm-to-table',
]

descriptors = [
    'fusion','confluence','barage','face full','mind blower','mouth full','explosion','plethora','cacophany','symphony','kamikaze',
]

bridge_words = [
    'inspired','influenced','infused','violently shaken','invigorated',
]

bridge_words2 = [
    'featuring','with','wrapped with','entangled in','created with','massaged on','massaged with','fully expressed with','deconstructed with','deconstructed on','with drippings of'
]

singles = ['booze','washed egg','mothers milk','salmon feet','water']

@app.route('/', strict_slashes=False)
@app.route('/<N>', strict_slashes=False)
def index(N=5):
    N = int(N)
    items = [gen_one() for i in range(N)]
    return render_template('index.html', items=items)

def gen_one():
    try:
        starter = np.random.choice(descriptors).title()
        template = '''
        %s of %s and %s %s %s %s %s %s and %s %s
    ''' % (
        starter,
        np.random.choice(flavor_names).lower(),
        np.random.choice(flavor_names).lower(),
        np.random.choice(bridge_words),
        np.random.choice(food_names).lower(),
        np.random.choice(bridge_words2),
        np.random.choice(cooking_styles),
        np.random.choice(food_names).lower(),
        np.random.choice(cooking_styles2),
        np.random.choice(food_names).lower(),
    )
    except: 
        template = np.random.choice(singles)
    return {'text':template,'price':np.random.randint(8,22)}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
