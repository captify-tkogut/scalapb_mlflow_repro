# README

## What is being tested

We have 3 proto files from scalapb project:
- mlflow version which we get as generated code from mlflow package
- v0.5.0 which is almost identical to mlflow one (package name is different)
- v0.8.2 which is a lot newer with more options

There are 3 packages that each uses one of the version in a function.
All 3 functions are being called in main. 

That tries to simulate different dependencies providing the same scalapb file.

## Preparation
Create custom python evn with tooling of your liking.  
`conda create -n repro_error python==3.9 -y`
   
Install dependencies

```bash
pip install -r requirments.txt
```

Run protos generation:  
```bash
gen_protos.sh
```



## Getting the bug
Run:  

```bash
python main.py
```


You should get the following output:

```
 python main.py                
Traceback (most recent call last):
  File "/Users/tkogut/repro_error/main.py", line 1, in <module>
    from  pkg_ml.lib_ml import do_sth_mlflow
  File "/Users/tkogut/repro_error/pkg_ml/lib_ml.py", line 1, in <module>
    from mlflow.protos.scalapb import scalapb_pb2
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/__init__.py", line 32, in <module>
    import mlflow.tracking._model_registry.fluent
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/tracking/__init__.py", line 8, in <module>
    from mlflow.tracking.client import MlflowClient
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/tracking/client.py", line 15, in <module>
    from mlflow.entities import ViewType
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/entities/__init__.py", line 6, in <module>
    from mlflow.entities.experiment import Experiment
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/entities/experiment.py", line 2, in <module>
    from mlflow.entities.experiment_tag import ExperimentTag
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/entities/experiment_tag.py", line 2, in <module>
    from mlflow.protos.service_pb2 import ExperimentTag as ProtoExperimentTag
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/protos/service_pb2.py", line 18, in <module>
    from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/mlflow/protos/scalapb/scalapb_pb2.py", line 29, in <module>
    options = _descriptor.FieldDescriptor(
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/google/protobuf/descriptor.py", line 561, in __new__
    _message.Message._CheckCalledFromGeneratedFile()
TypeError: Descriptors cannot not be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
```

## Trying downgrade
Downgrade to protobuf 3.20.x

```
pip install protobuf==3.20.1
```

Run again `gen_protos.sh` and `python main.py`.

What we get is:

```
Traceback (most recent call last):
  File "/Users/tkogut/repro_error/main.py", line 2, in <module>
    from pkg_082.lib_082 import do_sth_082
  File "/Users/tkogut/repro_error/pkg_082/lib_082.py", line 1, in <module>
    from pkg_050 import scalapb_pb2
  File "/Users/tkogut/repro_error/pkg_050/scalapb_pb2.py", line 17, in <module>
    DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rscalapb.proto\x12\x07scalapb\x1a google/protobuf/descriptor.proto\"L\n\x0eScalaPbOptions\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x14\n\x0c\x66lat_package\x18\x02 \x01(\x08\x12\x0e\n\x06import\x18\x03 \x03(\t\"!\n\x0eMessageOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\"\x1c\n\x0c\x46ieldOptions\x12\x0c\n\x04type\x18\x01 \x01(\t:G\n\x07options\x12\x1c.google.protobuf.FileOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.ScalaPbOptions:J\n\x07message\x12\x1f.google.protobuf.MessageOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.MessageOptions:D\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xfc\x07 \x01(\x0b\x32\x15.scalapb.FieldOptionsB\x18\n\x16\x63om.trueaccord.scalapb')
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/google/protobuf/descriptor_pool.py", line 219, in AddSerializedFile
    file_desc = self._ConvertFileProtoToFileDescriptor(file_desc_proto)
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/google/protobuf/descriptor_pool.py", line 774, in _ConvertFileProtoToFileDescriptor
    message_desc = self._ConvertMessageDescriptor(
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/google/protobuf/descriptor_pool.py", line 918, in _ConvertMessageDescriptor
    self._CheckConflictRegister(desc, desc.full_name, desc.file.name)
  File "/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/google/protobuf/descriptor_pool.py", line 191, in _CheckConflictRegister
    raise TypeError(error_msg)
TypeError: Conflict register for file "scalapb.proto": scalapb.ScalaPbOptions is already defined in file "scalapb/scalapb.proto". Please fix the conflict by adding package name on the proto file, or use different name for the duplication.
(repro_error) 
```



## Other observations

### Everything generated from a single compiler
When both protos are generated with the sam pb >= 3.20.x (also for 4.20.x) works with no problems.

```python
# from  pkg_ml.lib_ml import do_sth_mlflow
from pkg_082.lib_082 import do_sth_082
from pkg_050.lib_050 import do_sth_052
if __name__ == "__main__":
    do_sth_082()
    do_sth_052()
    # do_sth_mlflow()
```

### 3.19

mlflow regenerated python scalapb last year with [this commit](https://github.com/mlflow/mlflow/commit/1e2b4ed051bc760fd3e7d69149e1fbc1f7928edf).

`pip install  protobuf==3.19`

gives 

```▶ python main.py             
Traceback (most recent call last):
  File "/Users/tkogut/repro_error/main.py", line 2, in <module>
    from pkg_082.lib_082 import do_sth_082
  File "/Users/tkogut/repro_error/pkg_082/lib_082.py", line 1, in <module>
    from pkg_050 import scalapb_pb2
  File "/Users/tkogut/repro_error/pkg_050/scalapb_pb2.py", line 5, in <module>
    from google.protobuf.internal import builder as _builder
ImportError: cannot import name 'builder' from 'google.protobuf.internal' (/opt/homebrew/Caskroom/miniforge/base/envs/repro_error/lib/python3.9/site-packages/google/protobuf/internal/__init__.py)
(repro_error)
```


which is a known problem on [stackoverflow](https://stackoverflow.com/questions/71759248/importerror-cannot-import-name-builder-from-google-protobuf-internal)