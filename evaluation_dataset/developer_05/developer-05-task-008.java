public void visitClassDeclaration(ClassDeclaration d) {
		d.accept(pre);
		for (TypeParameterDeclaration tpDecl : d.getFormalTypeParameters()) {
			tpDecl.accept(this);
		}
		for (FieldDeclaration fieldDecl : d.getFields()) {
			fieldDecl.accept(this);
		}
		for (MethodDeclaration methodDecl : d.getMethods()) {
			methodDecl.accept(this);
		}
		for (TypeDeclaration typeDecl : d.getNestedTypes()) {
			typeDecl.accept(this);
		}
		for (ConstructorDeclaration ctorDecl : d.getConstructors()) {
			ctorDecl.accept(this);
		}
		d.accept(post);
	}