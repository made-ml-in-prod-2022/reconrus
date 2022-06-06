import requests
from http import HTTPStatus

import click


@click.command()
@click.option("--ip", type=str)
@click.option("--port", type=int)
@click.option("--age", type=int)
@click.option("--sex", type=int)
@click.option("--cp", type=int)
@click.option("--trestbps", type=int)
@click.option("--chol", type=int)
@click.option("--fbs", type=int)
@click.option("--restecg", type=int)
@click.option("--thalach", type=int)
@click.option("--exang", type=int)
@click.option("--oldpeak", type=float)
@click.option("--slope", type=int)
@click.option("--ca", type=int)
@click.option("--thal", type=int)
def main(
    ip: str,
    port: int,
    age: int,
    sex: int,
    cp: int,
    trestbps: int,
    chol: int,
    fbs: int,
    restecg: int,
    thalach: int,
    exang: int,
    oldpeak: float,
    slope: int,
    ca: int,
    thal: int,
):
    url = f"http://{ip}:{port}/predict"
    response = requests.post(
        url,
        json={
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal,
        },
    )
    if response.status_code == HTTPStatus.OK:
        print(f"Label: {response.text}")
    else:
        print(f"Error occured. " f"Status code: {response.status_code}")


if __name__ == "__main__":
    main()
