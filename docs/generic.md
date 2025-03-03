GET apirest.php/:itemtype/ => List all items of type :itemtype
POST apirest.php/:itemtype/ => Create a new item of type :itemtype

GET apirest.php/:itemtype/:id => Get item of type :itemtype with id :id
DELETE apirest.php/:itemtype/:id => Delete item of type :itemtype with id :id
PUT apirest.php/:itemtype/:id => Update item of type :itemtype with id :id

GET apirest.php/:itemtype/:id/:subitemtype/ => List all subitems of type :subitemtype for item of type :itemtype with id :id
POST apirest.php/:itemtype/:id/:subitemtype/ => Create a new subitem of type :subitemtype for item of type :itemtype with id :id

