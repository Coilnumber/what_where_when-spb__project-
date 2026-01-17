import { createBrowserRouter } from 'react-router-dom'

import App from './App.tsx';

export const router = createBrowserRouter([
  {
    element: <MainLayout />,
    children: [
      {
        path: '/',
        element: <App />,
      },

    ],
  },


])
