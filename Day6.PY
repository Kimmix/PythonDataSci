col_names = ['pregnant', 'glucose', 'bp', 'skin',
             'insulin', 'bmi', 'pedigree', 'age', 'label']

# load dataset pima = pd.read_csv("pima-indians-diabetes.csv", header=None, names=col_names)

pima.head()

feature_cols = ['pregnant', 'insulin', 'bmi',
                'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols]  # Features
y = pima.label  # Target variable
