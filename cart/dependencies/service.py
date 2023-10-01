import inspect
from typing import Type, List
from fastapi import Depends
from cart.utils.repositories import BaseRepository
from cart.utils.services import BaseService
from cart.dependencies.repository import get_repositories


def get_service(service_type: Type[BaseService]):
    """
    Returns an instance of the service with the needed repositories.
    The needed repositories are the ones declared in its __init__ method with type hint.
    By definition a repository inherit from BaseRepository.
    """
    repository_classes = [
        Repo for Repo in service_type.__init__.__annotations__.values()
        if BaseRepository in inspect.getmro(Repo)
    ]

    def _get_service(repositories: Type[List[BaseRepository]] = Depends(get_repositories(*repository_classes))):
        return service_type(*repositories)

    return _get_service
