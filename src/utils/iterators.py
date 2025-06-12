from typing import Dict, Hashable, Iterable, List, Tuple, TypeVar

K = TypeVar("K", bound=Hashable)
T = TypeVar("T")


def partition(it: Iterable[Tuple[K, T]]) -> Dict[K, List[T]]:
    out: Dict[K, List[T]] = {}

    for k, t in it:
        group_list = out.get(k, [])
        group_list.append(t)
        out[k] = group_list

    return out
