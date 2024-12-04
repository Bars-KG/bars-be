from typing import Callable

from api.dataclasses.detail_page import DetailFieldDataClass


# field creators for manual usage outside of builder context
def section_field(name: str) -> DetailFieldDataClass:
    return DetailFieldDataClass(type="section", value=name)


def literal_field(
    label: str, value: str, caster: Callable[[str], str] = str
) -> DetailFieldDataClass:
    return DetailFieldDataClass(type="literal", label=label, value=caster(value))


def hyperlink_field(
    label: str,
    value: str,
    link: str,
    value_caster: Callable[[str], str] = str,
    link_caster: Callable[[str], str] = str,
) -> DetailFieldDataClass:
    return DetailFieldDataClass(
        type="hyperlink",
        label=label,
        value=value_caster(value),
        hyperlink=link_caster(link),
    )

def separator_field() -> DetailFieldDataClass:
    return DetailFieldDataClass(type="separator")

def image_field(image_url: str) -> DetailFieldDataClass:
    return DetailFieldDataClass(type="image", value=image_url)


# main builder
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

# field builders
def section_builder(name: str) -> Callable[[dict], DetailFieldDataClass]:
    return lambda _: section_field(name)


def literal_builder(
    label: str, key: str, caster: Callable[[str], str] = str
) -> Callable[[dict], DetailFieldDataClass]:
    return lambda d: literal_field(label, d[key]["value"], caster)


def hyperlink_builder(
    label: str,
    key: str,
    link_key: str,
    value_caster: Callable[[str], str] = str,
    link_caster: Callable[[str], str] = str,
) -> Callable[[dict], DetailFieldDataClass]:
    return lambda d: hyperlink_field(
        label, d[key]["value"], d[link_key]["value"], value_caster, link_caster
    )

def image_builder(
    key: str
) -> Callable[[dict], DetailFieldDataClass]:
    return lambda d: image_field(d[key]["value"])