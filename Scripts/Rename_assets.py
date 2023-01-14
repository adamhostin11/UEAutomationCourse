import unreal


def rename_assets(search_pattern, replace_pattern, use_case):
    # instances of UE classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    # get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    counter = 0

    unreal.log("Selected {} assets".format(num_assets))

    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)
        if string_lib.contains(asset_name, search_pattern, use_case=use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            editor_util.rename_asset(asset, string_lib.replace(asset_name, search_pattern, replace_pattern, search_case=search_case))
            counter += 1
        else:
            unreal.log("{} has no match for the pattern".format(asset.get_name()))

    unreal.log("{} of {} assets were replaced".format(counter.__str__(), num_assets.__str__()))


rename_assets("AAA", "ABC", False)
