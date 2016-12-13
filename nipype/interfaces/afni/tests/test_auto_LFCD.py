# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import LFCD


def test_LFCD_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    autoclip=dict(argstr='-autoclip',
    ),
    automask=dict(argstr='-automask',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    ),
    mask=dict(argstr='-mask %s',
    ),
    out_file=dict(argstr='-prefix %s',
    name_source=[u'in_file'],
    name_template='%s_afni',
    ),
    outputtype=dict(),
    polort=dict(argstr='-polort %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    thresh=dict(argstr='-thresh %f',
    ),
    )
    inputs = LFCD.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_LFCD_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = LFCD.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
