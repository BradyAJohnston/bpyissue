import bpy

def _update_handler(self, context: bpy.types.Context) -> None:
    print("Updating property!")

def main():
    bpy.types.Object.custom_property = bpy.props.FloatProperty(update=_update_handler)
    obj = bpy.data.objects["Cube"]
    print(obj)


if __name__ == "__main__":
    main()
