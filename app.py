
from flask import Flask, render_template, Markup
import numpy as np
import pandas as pd

app = Flask(__name__, static_url_path = '')

foods = pd.read_csv('foods_filter_names.csv')
flavors = pd.read_csv('flavors.csv')

flavor_names = flavors.name.values.flatten()
food_names = foods.name.values.flatten()
cooking_styles = [
    'grilled','fried','deep fried', 'braised','skillet fried','pan fried','boiled','steamed','sous vide','flambee','fast fry','foamed',
]

cooking_styles2 = [
    'British','American','Thai','Chinese','Southern','Mid-Western','Indian', "Creole",'Greek','Middle Eastern', 'gluten free',
]

adjectives = [
    'fusion','confluence','barage','face full','mind blower','mouth full','explosion','plethora','cacophany','symphony','kamikaze'
]

@app.route('/', strict_slashes=False)
@app.route('/<N>', strict_slashes=False)
def index(N=1):
    N = int(N)
    items = [gen_one() for i in range(N)]
    return render_template('index.html', items=items)

def gen_one():
    starter = np.random.choice(adjectives).title()
    template = '''
        %s of %s and %s inspired %s featuring %s %s and %s %s
    ''' % (
        starter,
        np.random.choice(flavor_names),
        np.random.choice(flavor_names),
        np.random.choice(food_names),
        np.random.choice(cooking_styles),
        np.random.choice(food_names),
        np.random.choice(cooking_styles2),
        np.random.choice(food_names),
    )
    return template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
