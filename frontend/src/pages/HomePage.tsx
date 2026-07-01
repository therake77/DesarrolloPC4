import { Box, Card, Flex, Heading, Text } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import {
  LuChartBar,
  LuFolder,
  LuMenu,
  LuSettings,
  LuUsers,
} from "react-icons/lu";
import { useNavigate, useParams } from "react-router";
import Header from "../components/Header";
import Sidebar from "../components/Sidebar";
import type { NavItem, User } from "../types/layout";
 
const NAV_ITEMS: NavItem[] = [
  { label: "Dashboard", icon: LuMenu },
  { label: "Users",     icon: LuUsers },
  { label: "Projects",  icon: LuFolder },
  { label: "Analytics", icon: LuChartBar },
  { label: "Settings",  icon: LuSettings },
];
 
const EMPTY_USER: User = { id: 0, name: "", email: "example@example.com" };
 
export default function HomePage() {
  const navigate = useNavigate();
  const { id } = useParams();
 
  // Kept for future auth use
  const token = localStorage.getItem("access_token");
 
  const [currUser, setCurrUser] = useState<User>(EMPTY_USER);
  const [active, setActive] = useState("Dashboard");
 
  useEffect(() => {
    if (!id) {
      navigate("/login");
      return;
    }
 
    const userId = Number(id);
 
    if (Number.isNaN(userId)) {
      navigate("/login");
      return;
    }
 
    fetch(`http://localhost:8000/api/users/${userId}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((res) =>
        setCurrUser({ id: res.id, name: res.name, email: res.email })
      )
      .catch((err) => {
        console.error(err);
        navigate("/login");
      });
  }, [id, navigate]);
 
  return (
    <Flex minH="100vh" flexDir="column">
      <Header user={currUser} />
 
      <Flex flex={1} overflow="hidden">
        <Sidebar
          navItems={NAV_ITEMS}
          active={active}
          onNavigate={setActive}
          user={currUser}
        />
 
        {/* ── Main content ── */}
        <Box flex={1} bg="gray.50" p={8} overflowY="auto">
          <Heading size="lg" mb={2} color="gray.800">
            {active}
          </Heading>
          <Text color="gray.500" mb={6}>
            This is the {active.toLowerCase()} section.
          </Text>
 
          <Card.Root maxW="600px">
            <Card.Body>
              <Text color="gray.400" textAlign="center" py={10}>
                Your content goes here.
              </Text>
            </Card.Body>
          </Card.Root>
        </Box>
      </Flex>
    </Flex>
  );
}