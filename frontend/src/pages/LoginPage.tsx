import { Box, Button, Card, chakra, Field, Heading, Input, Stack, Text } from "@chakra-ui/react";
import { jwtDecode } from "jwt-decode";
import { useState } from "react";
import { Link as RouterLink, useNavigate } from "react-router";

const StyledLink = chakra(RouterLink)

interface Token{
    access_token : string
    token_type : string
};

export default function LoginPage(){
    
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    const handleLogin = async (email : string, password : string) => {
        const res = await fetch("http://localhost:8000/api/users/login",{
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify({
                email : email,
                password : password 
            })
        })

        if(!res.ok){
            console.log("Error llamando a la API")
            return;
        }
        
        const token : Token = await res.json()
        const payload = jwtDecode(token.access_token);

        localStorage.setItem("access_token",token.access_token)
        localStorage.setItem("token_type",token.token_type)
        console.log(payload);
        navigate(`/home/${payload.sub!}`)

    }
    
    
    
    return (
        <Box alignItems="center" display="flex" justifyContent={"center"} minH={"100vh"} bg="gray.50">
            <Card.Root w={{ base: "90%", sm: "400px" }} p={8} boxShadow="md">
                <Card.Header pb={2}>
                <Heading size="xl" textAlign="center">
                    Welcome back
                </Heading>
                <Text color="gray.500" textAlign="center" mt={1}>
                    Sign in to your account
                </Text>
                </Card.Header>
        
                <Card.Body>
                <Stack gap={5}>
                    <Field.Root>
                    <Field.Label>Email</Field.Label>
                    <Input type="email" placeholder="you@example.com" value={email} onChange={ (e) =>{ setEmail(e.target.value)}} />
                    </Field.Root>
        
                    <Field.Root>
                    <Field.Label>Password</Field.Label>
                    <Input type="password" placeholder="••••••••" value={password} onChange={(e) => {setPassword(e.target.value)}} />
                    </Field.Root>
        
                    <Button colorPalette="blue" size="md" width="full" mt={2} onClick={() => handleLogin(email,password)}>
                    Log in
                    </Button>
                </Stack>
                </Card.Body>
        
                <Card.Footer justifyContent="center" pt={2}>
                <Text fontSize={"sm"} color={"gray.600"}>
                    Don't have an account?{" "}
                    <StyledLink to="/register" color="blue.500" fontWeight="medium">
                    Register
                    </StyledLink>
                </Text>
                </Card.Footer>
            </Card.Root>
        </Box>
    );
}