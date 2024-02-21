# from unittest import result
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/stage_one', methods=['GET'])
def stage_one():
    # Get 'a' from query parameters
    a = request.args.get('a', default=0, type=float)
    
    def f(x):
        return 3 * x - 3
    

    results = {"approach_minus": [], "approach_plus": []}


    t = 0.1
    while t > 0.0000001:
        results["approach_minus"].append({"x": round(a - t, 7), "f(x)": round(f(a - t), 7)})
        t = t / 10
    
    t = 0.1
    while t > 0.0000001:
        results["approach_plus"].append({"x": round(a + t, 7), "f(x)": round(f(a + t), 7)})
        t = t / 10
    
    return jsonify(results)



@app.route('/stage_two', methods=['GET'])
def stage_two():
    a = request.args.get('a', default=0, type=float)
    results = {"approach_minus": [], "approach_plus": []}

    def f(x):
        return pow(x, 3) + 2 * pow(x, 2)
    
    t = 0.1
    while t > 0.000001:
        results["approach_minus"].append({"x": round(a - t, 7), "f(x)": round(f(a - t), 7)})
        t = t / 10

    t = 0.1
    while t > 0.000001:
        results["approach_plus"].append({"x": round(a - t, 7), "f(x)": round(f(a + t), 7)})
        t = t / 10
    
    return jsonify(results = results)




@app.route('/stage_three', methods=['GET'])
def stage_three():

    a = request.args.get('a', default=0, type=float)
    results = {"tilnæermingverdig": [],"approach_minus": [], "approach_plus": []}

    def f(x):
        # lim ---> a || lim(x**3 + 2x**2)
        return pow(x, 3) + 2 * pow(x, 2) - 6
    
    t = 0.1
    while t > 0.000001:
        results["approach_minus"].append({"x": round(a - t, 7), "f(x)": round(f(a - t), 7)})
        t = t / 10

    t = 0.1
    while t > 0.000001:
        results["approach_plus"].append({"x": round(a - t, 7), "f(x)": round(f(a + t), 7)})
        t = t / 10
    
    results["tilnæermingverdig"].append("lim--->a(x**3 + 2x**2 + 3x -6 )")
    return jsonify(results = results)





@app.route('/sammenlikn', methods=['GET'])
def sammenlikn():

    a = request.args.get('stage_one_two', default=0, type=str)
    results = {"stg1": [],"stg2": [], "forklaring": []}
    results["stg1"].append("f(x): 11.7 er konstant og  x: 4.9 er også konstant")
    results["stg2"].append("f(x): 11.7 er konstant og  x: 4.9 er også konstant")
    return jsonify(results = results)


if __name__ == '__main__':
    app.run(debug=True)

