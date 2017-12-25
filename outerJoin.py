import pandas as pd

def leftOuterJoin(left_df, right_df, key):
    right_df['tmp'] = '@'
    join_df = left_df.merge(right_df[['tmp', key]], how='left', on=key)
    join_df = join_df[pd.isnull(join_df['tmp'])]
    join_df.drop('tmp', axis=1, inplace=True)
    right_df.drop('tmp', axis=1, inplace=True)
    return join_df

def rightOuterJoin(left_df, right_df, key):
    return leftOuterJoin(right_df, left_df, key)


existing_df = pd.DataFrame.from_dict([{'a': 1, 'b':2}, {'a': 11, 'b':22}, {'a': 111, 'b':222}])
new_df = pd.DataFrame.from_dict([{'a': 11, 'c':33}, {'a': 111, 'c':333}, {'a': 1111, 'c':3333}])
key = 'a'

print leftOuterJoin(existing_df, new_df, key)
print rightOuterJoin(existing_df, new_df, key)
