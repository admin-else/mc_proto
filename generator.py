import jinja2
import json

jenv = jinja2.Environment(
    loader=jinja2.PackageLoader("generator"), trim_blocks=True, lstrip_blocks=True
)

with open("minecraft-data/data/pc/1.21.3/protocol.json") as f:
    protocol = json.load(f)

protocol_version = 69

prefix = f"mc_proto_{protocol_version}"

current_packet = None
container_stack = []


def container_stack_push(data):
    container_stack.append(data)
    return ""


def container_stack_pop():
    container_stack.pop()
    return ""


def set_current_packet(packet):
    global current_packet
    current_packet = packet
    return ""


def parse(data, prefix):
    output = {}
    for k, v in data.items():
        if k != "types":
            for k, v in parse(v, prefix + "_" + k).items():
                output[k] = v
            continue
        for k, v in data["types"].items():
            output[prefix + "_" + k] = v
    return output


def get(data, f, **kwargs):
    global current_packet
    current_packet_cpy: str = current_packet
    current_packet_cpy = current_packet_cpy.removeprefix(prefix + "_")
    current_packet_cpy = current_packet_cpy.split("_")
    proto_copy = protocol.copy()
    types = proto_copy["types"]
    for i, k in enumerate(current_packet_cpy):
        if k in proto_copy:
            proto_copy = proto_copy[k]
            if "types" in proto_copy:
                for k, v in proto_copy["types"].items():
                    types[k] = (v, "_".join(current_packet_cpy[i:]))
                break
        else:
            break

    if type(data) is str:
        t = data
    else:
        t, data = data

    if t in types and types[t] != "native":
        return render("common", f, typename=t, prefix=prefix, **kwargs)

    if type(data) is dict:
        for k, v in data.items():
            kwargs[k] = v
        return render(t, f, **kwargs)
    else:
        return render(t, f, data=data, **kwargs)


def render(*args, **kwargs):
    kwargs["render"] = render
    kwargs["get"] = get
    kwargs["set_current_packet"] = set_current_packet
    kwargs["container_stack_push"] = container_stack_push
    kwargs["container_stack_pop"] = container_stack_pop
    kwargs["current_packet"] = current_packet
    try:
        return jenv.get_template("/".join(args) + ".j2").render(kwargs).strip()
    except Exception as e:
        return f"/* {type(e)}: {e} */"


prefixed_data = parse(protocol, prefix)
prefixed_data = {k: v for k, v in prefixed_data.items() if not v == "native"}


# print(json.dumps(data))
header = render("common", "header", data=prefixed_data)
with open("gen.h", "w") as f:
    f.write(header)
