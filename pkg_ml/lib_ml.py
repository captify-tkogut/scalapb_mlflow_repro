from mlflow.protos.scalapb import scalapb_pb2

def do_sth_mlflow():
    a = scalapb_pb2.ScalaPbOptions()
    a.package_name = "package set"
    print(f"hello from mlflow {a}")