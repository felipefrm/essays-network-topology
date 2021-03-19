import ast

def normalize_final_score_and_criteria_score(input, output):

    df = pd.read_csv(filename)

    for i in range(len(df)):
        
        final_score = float(df.loc[i]['final_score'].replace(',', '.').strip())
        df.loc[i, 'final_score'] = final_score * 100 if final_score <= 10 else final_score

        scores = ast.literal_eval(df.loc[i]['criteria_scores'])
        scores = {k: str(float(v * 100)) if float(v) <= 2 else v for k, v in scores.items()}
        df.loc[i, 'criteria_scores'] = str(scores)

    df = df[df['final_score'] != 0]

    df.to_csv(output)



normalize_final_score_and_criteria_score('data/edit.csv', 'data/essays_clean.csv')