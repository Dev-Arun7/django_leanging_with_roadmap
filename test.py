    # NEW: Validate uploaded document
    def clean_document(self):
        document = self.cleaned_data.get("document")

        # No document uploaded? That's okay.
        if not document:
            return document

        # Allow only PDF files
        if not document.name.lower().endswith(".pdf"):
            raise forms.ValidationError("Only PDF files are allowed.")

        # Maximum file size: 5 MB
        if document.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File size cannot exceed 5 MB.")

        return document