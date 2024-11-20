export enum Role {
    ADMIN = "ADMIN",
    STANDARD = "STANDARD",
}

export interface User {
    id: string;
    login: string;
    email: string;
    role: Role;
}
