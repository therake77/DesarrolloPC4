import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, Navigate, RouterProvider } from 'react-router';
import { ChakraProvider, defaultSystem } from '@chakra-ui/react';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import HomePage from './pages/HomePage';
import ProtectedRoute from './components/ProtectedRoute';

const router = createBrowserRouter([
  {path : "/login", element : <LoginPage/> },
  {path : "/register", element : <RegisterPage/>},
  {path : "/home/:id", element: <ProtectedRoute><HomePage/></ProtectedRoute>},
  {path : "*", element: <Navigate to="/login" replace/>}
])

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ChakraProvider value={defaultSystem}>
      <RouterProvider router={router}/>
    </ChakraProvider>
  </React.StrictMode>
)
