# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import ThresholdStatistics


def test_ThresholdStatistics_inputs():
    input_map = dict(contrast_index=dict(mandatory=True,
    ),
    extent_threshold=dict(usedefault=True,
    ),
    height_threshold=dict(mandatory=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    paths=dict(),
    spm_mat_file=dict(copyfile=True,
    mandatory=True,
    ),
    stat_image=dict(copyfile=False,
    mandatory=True,
    ),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    )
    inputs = ThresholdStatistics.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ThresholdStatistics_outputs():
    output_map = dict(clusterwise_P_FDR=dict(),
    clusterwise_P_RF=dict(),
    voxelwise_P_Bonf=dict(),
    voxelwise_P_FDR=dict(),
    voxelwise_P_RF=dict(),
    voxelwise_P_uncor=dict(),
    )
    outputs = ThresholdStatistics.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
