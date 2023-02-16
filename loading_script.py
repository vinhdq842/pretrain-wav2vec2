import datasets
import os
import glob

_CITATION = "DUMMY CITATION"

_DESCRIPTION = "DUMMY DESCRIPTION"

_URL = "DUMMY URL"

class RawAudioConfig(datasets.BuilderConfig):
    def __init__(self,**kwargs):
        super(RawAudioConfig,self).__init__(version=datasets.Version("25.04.2001",""),**kwargs)

class RawAudioDataset(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [RawAudioConfig(name="raw",description="'Raw' speech.")]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "file": datasets.Value("string"),
                    "audio": datasets.features.Audio(sampling_rate=16_000),
                }
            ),
            homepage=_URL,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"data_dir": self.config.data_dir}),
        ]

    def _generate_examples(self, data_dir):
        transcripts_glob = os.path.join(data_dir,"*.wav")
        for transcript_file in glob.glob(transcripts_glob):
            key = transcript_file.split('/')[-1][:-4]
            example = {
                "file": transcript_file,
                "audio": transcript_file,
            }
            yield key, example