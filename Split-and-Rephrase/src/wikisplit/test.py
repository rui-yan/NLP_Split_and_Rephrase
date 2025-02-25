import evaluate
import os

def main():
    model_name = 'sprp_onmt_copy_512'

    base_path = '/dfs/scratch0/ruiyan/NLP'

    moses_path = base_path + '/mosesdecoder'

    test_dirs_path_prefix = base_path + '/Split-and-Rephrase/evaluation-directories/wikisplit/test/'

    # the file containing the ids of the test sentences
    test_sent_ids_path = base_path + '/Split-and-Rephrase/benchmark/wikisplit/complex-sents/test.id'

    # a directory that will hold single sentence files for the hypotheses
    test_hypothesis_sents_dir = base_path + '/phrasing/models/wikisplit/test_complex_output_sents/'
    if not os.path.exists(test_hypothesis_sents_dir):
        os.mkdir(test_hypothesis_sents_dir)

    test_target = base_path + '/phrasing/models/wikisplit/test.complex.unique.output'

    print('starting multi-ref evaluation...')
    avg_bleu, avg_tokens_per_sent, avg_simple_sents_per_complex = evaluate.evaluate_avg_concat_bleu(moses_path,
                                                                                                    test_sent_ids_path,
                                                                                                    test_hypothesis_sents_dir,
                                                                                                    test_target,
                                                                                                    test_dirs_path_prefix)

    print('avg BLEU:{} avg tokens/sent: {} avg split: {}'.format(avg_bleu, avg_tokens_per_sent,
                                                                 avg_simple_sents_per_complex))
    return

if __name__ == '__main__':
    main()
