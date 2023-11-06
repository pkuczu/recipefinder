const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const port = 3001;

app.use(bodyParser.json());

app.post('/addIngredients', (req, res) => {
  const ingredients = req.body.ingredients;

  // TODO: Insert ingredients into your SQL database here

  res.json({ message: 'Ingredients added to the database' });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});