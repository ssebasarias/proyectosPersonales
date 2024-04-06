import React from 'react';
import { TodoCounter } from './TodoCounter';
import { TodoSearch } from './TodoSearch';
import { TodoList } from './TodoList';
import { CreateTodoButton } from './CreateTodoButton';
import { TodoItem } from './TodoItem';


const defaultTodos = [
  {text: 'Poner canción para bailar', completed:true},
  {text: 'Cortar cebolla', completed: true},
  {text: 'Cortar tomate', completed: false},
  {text: 'Cortar cilantro', completed: false},
  {text: 'Combinar los ingredientes', completed: false},
];

function App() {

    // IMPORTANTE: El estado de una interaccion es inmutable, por eso requiere de una funcion controlada por React para modificarse.
  /*
  Esto se hace mediante un arreglo que envia los valores a React, teniendo el primer dato de arreglo como el valor inicial y
  el segundo valor del array como el nuevo valor que se le envia
  */

  const [todos, setTodos] = React.useState(defaultTodos);
  const [searchValue, setSearchValue] = React.useState('');

  console.log('El usuario busco el Todo ' + searchValue); // Para confirmar que React si este escuchando el input de TodoSearch

  const completedTodos = todos.filter(todos => !!todos.completed).length;
  const total = todos.length;

  const searchedTodos = todos.filter(
    (todo) => {
      
      // función texto sin tildes
      const noTildes = (text) => {
        return text.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
      };

      // Normalizando texto sin tildes y a Lower Case
      const TodoTextLC = noTildes(todo.text.toLowerCase());
      const searchTextLC = noTildes(searchValue.toLowerCase());

      //renderizar con filtro
      return TodoTextLC.includes(searchTextLC);
    }
  );

  const completeTodo = (text) => {
    const newTodos = [...todos];
    const todoIndex = newTodos.findIndex(
      (todo) => todo.text === text
    );
    newTodos[todoIndex].completed = true;
    setTodos(newTodos);
  }

  const deleteTodo =(text) => {
    const newTodos = [...todos];
    const todoIndex = newTodos.findIndex(
      (todo) => todo.text === text
    );
    newTodos.splice(todoIndex, 1);
    setTodos(newTodos);
  }

  return (
    <>

    <TodoCounter completed={completedTodos} total={total} />
    <TodoSearch
    searchValue = {searchValue}
    setSearchValue = {setSearchValue}
    />

    <TodoList>
      {searchedTodos.map(todos => (
        <TodoItem 
        key={todos.text}
        text={todos.text}
        completed={todos.completed}
        onComplete = {() => completeTodo(todos.text)}
        onDelete = {() => deleteTodo(todos.text)}
        />
      ))}
    </TodoList>

    <CreateTodoButton />

    </>
  );
}

export default App;
