import {
  Box,
  Button,
  Card,
  chakra,
  Field,
  Heading,
  Input,
  Stack,
  Text,
} from "@chakra-ui/react";
import { useState } from "react";
import { Link as RouterLink, useNavigate } from "react-router";

const StyledLink = chakra(RouterLink);



export default function RegisterPage() {

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const nav = useNavigate();

  const handleRegister = async () => {
    const res = await fetch("http://localhost:8000/api/users/register",{
      method: 'POST',
      body : JSON.stringify({
        name : name,
        email : email,
        password : password 
      }),
      headers : {
        'Content-Type' : 'application/json'
      }
    })

    if(!res.ok){
      console.log(res.statusText)
      return;
    }
    nav("/login")
  }


  return (
    <Box minH="100vh" display="flex" alignItems="center" justifyContent="center" bg="gray.50">
      <Card.Root w={{ base: "90%", sm: "400px" }} p={8} boxShadow="md">
        <Card.Header pb={2}>
          <Heading size="xl" textAlign="center">
            Regístrate
          </Heading>
        </Card.Header>
 
        <Card.Body>
          <Stack gap={5}>
            <Field.Root>
              <Field.Label>Nombre</Field.Label>
              <Input type="text" placeholder="Nombre" value={name} onChange={(e) => {setName(e.target.value)}} />
            </Field.Root>
 
            <Field.Root>
              <Field.Label>Email</Field.Label>
              <Input type="email" placeholder="you@example.com" value={email} onChange={(e) => {setEmail(e.target.value)}} />
            </Field.Root>
 
            <Field.Root>
              <Field.Label>Contraseña</Field.Label>
              <Input type="password" placeholder="••••••••" value={password} onChange={(e) => {setPassword(e.target.value)}} />
            </Field.Root>
 
            <Button colorPalette="blue" size="md" width="full" mt={2} onClick={handleRegister}>
              Regístrate
            </Button>
          </Stack>
        </Card.Body>
 
        <Card.Footer justifyContent="center" pt={2}>
          <Text fontSize="sm" color="gray.600">
            Tiene una cuenta?{" "}
            <StyledLink to="/login" color="blue.500" fontWeight="medium">
              Ingrese
            </StyledLink>
          </Text>
        </Card.Footer>
      </Card.Root>
    </Box>
  );
}