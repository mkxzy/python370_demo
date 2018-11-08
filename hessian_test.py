from dataclasses import dataclass

from pyhessian.client import HessianProxy
from pyhessian.protocol import cls_factory

NiceObject = cls_factory(
    name='com.gyxr.adam.dataservice.model.BrandItem',
    fields=['id', 'name']
)

nice_object = NiceObject(id="1", name='中文')

service = HessianProxy("http://localhost:8080/rmi/sync/brand")
service.save(nice_object)