from typing import Any, Callable

from api.dataclasses.detail_page import DetailFieldDataClass


def detail_builder(
    builders: list[Callable[[dict], DetailFieldDataClass]]
) -> Callable[[dict], list[DetailFieldDataClass]]:
    def build(d: dict):
        result = []
        for builder in builders:
            try:
                result.append(builder(d))
            except KeyError:
                pass

        return result

    return build


def section_builder(key: str) -> Callable[[dict], DetailFieldDataClass]:
    return lambda _: DetailFieldDataClass(type="section", value=key)


def literal_field(
    label: str, key: str, caster: Callable[[Any], Any] = str
) -> Callable[[dict], DetailFieldDataClass]:
    return lambda d: DetailFieldDataClass(
        type="literal", key=label, value=caster(d[key]["value"])
    )


def hyperlink_field(
    label: str,
    key: str,
    link_key: str,
    value_caster: Callable[[Any], Any] = str,
    link_caster: Callable[[Any], Any] = str,
) -> Callable[[dict], DetailFieldDataClass]:
    return lambda d: DetailFieldDataClass(
        type="hyperlink",
        key=label,
        value=value_caster(d[key]["value"]),
        hyperlink=link_caster(d[link_key]["value"]),
    )
